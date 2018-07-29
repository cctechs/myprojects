package parser

import (
	"github.com/myprojects/crawler/engine"
	"regexp"
)

// <a href="http://album.zhenai.com/u/1314495053" target="_blank">风中的蒲公英</a></th
const cityRe = `<th><a href="(http://album.zhenai.com/u/[0-9]+)"*[^>]*>([^<]+)</a></th>`

// 解析城市
func ParseCity(contents []byte) engine.ParseResult {
	re, err := regexp.Compile(cityRe)
	if err != nil {
		panic(err)
	}

	matches := re.FindAllSubmatch(contents, -1)

	result := engine.ParseResult{}
	for _, m := range matches {
		name := string(m[2])
		result.Items = append(result.Items, name)
		result.Requests = append(result.Requests,
			engine.Request{
				Url: string(m[1]),
				ParserFunc: func(bytes []byte) engine.ParseResult {
					return ParseProfile(bytes, name)
				},
			})
	}
	return result
}
