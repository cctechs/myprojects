package engine

import (
	"log"
	"github.com/myprojects/crawler/fetcher"
)

func  worker(r Request)(ParseResult, error){
	log.Printf("Fecthing %s", r.Url)
	body, err := fetcher.Fetch(r.Url)
	if err != nil {
		log.Printf("Fetcher:err, url:%s, %v", r.Url, err)
		return ParseResult{}, err
	}
	parseResult := r.ParserFunc(body)
	return parseResult, nil
}

func createWorker(out chan ParseResult, s Scheduler){
	in := make(chan Request)
	go func() {
		for{
			// tell schduler i am ready
			s.WorkerReady(in)
			request := <-in
			result, err := worker(request)
			if err != nil{
				continue
			}
			out <- result
		}
	}()
}