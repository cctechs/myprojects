package parser

import (
	"regexp"
	"fmt"
	"github.com/myprojects/crawler/engine"
)

func ParseCityList(contents []byte) engine.ParseResult {
	reg, err := regexp.Compile(
		`<a href="(http://www.zhenai.com/zhenghun/[a-z0-9]+)"+[^>]*>([^<]+)</a>`)
	if err != nil {
		panic(err)
	}
	matchs := reg.FindAllSubmatch(contents, -1)
	for _, v := range matchs {
		_ = v
		fmt.Printf("%s %s\n", string(v[1]), string(v[2]))
	}
	fmt.Printf("match found:%d\n", len(matchs))
}