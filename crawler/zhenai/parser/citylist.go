package parser

import (
	"regexp"
	"github.com/myprojects/crawler/engine"
)

const citylistRe = `<a href="(http://www.zhenai.com/zhenghun/[a-z0-9]+)"+[^>]*>([^<]+)</a>`

// 解析城市列表
func ParseCityList(contents []byte) engine.ParseResult {
	reg, err := regexp.Compile(citylistRe)
	if err != nil {
		panic(err)
	}
	result := engine.ParseResult{}
	matchs := reg.FindAllSubmatch(contents, -1)
	for _, m := range matchs {
		result.Items = append(result.Items, string(m[2]))
		result.Requests = append(result.Requests,engine.Request{
			Url:string(m[1]),
			ParserFunc:ParseCity,
		})
	}
	return result
}