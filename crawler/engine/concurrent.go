package engine

import "fmt"

type ConcurrentEngine struct {
	Scheduler Scheduler
	WorkCount int
}

type Scheduler interface {
	ReadyNotifier
	Submit(Request)
	WorkerChan()chan Request
	Run()
}

type ReadyNotifier interface {
	WorkerReady(chan Request)
}

func (e* ConcurrentEngine) Run(seeds ...Request)  {

	out :=make(chan ParseResult)
	e.Scheduler.Run()

	for i := 0; i < e.WorkCount; i++{
		createWorker(e.Scheduler.WorkerChan(), out, e.Scheduler)
	}

	for _, r := range  seeds{
		e.Scheduler.Submit(r)
	}

	itemCount := 0
	for{
		result := <-out
		for _, item := range result.Items{
			fmt.Printf("Got item:%v,  count:%v\n", item, itemCount)
			itemCount++
		}

		for _, request := range result.Requests{
			e.Scheduler.Submit(request)
		}
	}
}