package scheduler

import "github.com/myprojects/crawler/engine"

type SimpleScheduler struct {
	workerChan chan engine.Request
}

func (s* SimpleScheduler) ConfigureMasterWorkerChan(c chan engine.Request) {
	s.workerChan = c
}

func (s* SimpleScheduler) Submit(r engine.Request) {
	//!tmp check why
	go func() {
		s.workerChan<-r
	}()
}

