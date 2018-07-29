package main

import (
	"github.com/myprojects/crawler/engine"
	"github.com/myprojects/crawler/zhenai/parser"
	"github.com/myprojects/crawler/scheduler"
)

func main()  {
	//http://www.zhenai.com/zhenghun

	e := engine.ConcurrentEngine{
	    Scheduler:&scheduler.QueuedScheduler{},
	   	WorkCount:1000,
	}
	e.Run(
		engine.Request{
			Url:"http://www.zhenai.com/zhenghun",
			ParserFunc:parser.ParseCityList,
		})
	//printCityList(all)
}
