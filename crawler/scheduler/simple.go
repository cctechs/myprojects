package scheduler

import "github.com/myprojects/crawler/engine"

// 所有worker共用一个channel
type SimpleScheduler struct {
	workerChan chan engine.Request
}

func (s *SimpleScheduler) WorkerChan() chan engine.Request {
	return s.workerChan
}

func (s *SimpleScheduler) WorkerReady(chan engine.Request) {

}

func (s *SimpleScheduler) Run() {
	s.workerChan = make(chan engine.Request)
}


func (s* SimpleScheduler) Submit(r engine.Request) {
	//!tmp check why
	go func() {
		s.workerChan<-r
	}()
}

