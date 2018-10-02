package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

type myFunc func(map[string]string)

type MyServer struct {
	funcOp   chan myFunc
	funcDone chan struct{}
	quit chan struct{}
	mapData  map[string]string
}

func (this *MyServer) Add() {

}

func (this *MyServer) getCount() int {
	var count = 0
	select {
	case this.funcOp <- func(strings map[string]string) {
		count = len(strings)
	}:
		<-this.funcDone
	}
	return count
}

func (this *MyServer) run() {
	for {
		select {
		case fn := <-this.funcOp:
			fn(this.mapData)
			this.funcDone <- struct{}{}
			case <-this.quit:
				fmt.Printf("quit\n")
			return

		}
	}
}

func checkChannel(){
	mychannel := make(chan []int, 3)

	pendingQuereis := 0

	for i := 0; i < 3; i++ {
		pendingQuereis++
		go func(n int) {
			data := []int{1, 2, 3}
			mychannel <- data
		}(i)
	}

	for{
		if 0 == pendingQuereis{
			break
		}

		for k, v := range <-mychannel{
			fmt.Printf("%v, %v\n", k, v)
		}
		pendingQuereis--
	}


	fmt.Println("finished")
}

func main() {
	data := make(map[string]string)
	for i := 0; i < 10; i++ {
		k := fmt.Sprintf("%d", i)
		v := fmt.Sprintf("data%d", i)
		data[k] = v
	}
	svr := MyServer{funcOp: make(chan myFunc), funcDone: make(chan struct{}), quit:make(chan struct{}), mapData: data}
	go svr.run()
	n := svr.getCount()
	close(svr.quit)
	fmt.Println("count:", n)

	fmt.Printf("///////////////////////////\n")
	checkChannel()


	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	for{
		select {
		  case <-c:
		  	fmt.Printf("exit\n")
		    return
		}
	}


}
