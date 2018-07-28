package main

import (
	"github.com/myprojects/crawler/engine"
	"github.com/myprojects/crawler/zhenai/parser"
)

func main()  {
	//http://www.zhenai.com/zhenghun
	engine.Run(
		engine.Request{
			Url:"http://www.zhenai.com/zhenghun",
			ParserFunc:parser.ParseCityList,
		})
	//printCityList(all)
}
