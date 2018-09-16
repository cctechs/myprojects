package main

import (
	"fmt"
	"math/big"
	"math"
)

func main()  {
	d1 := big.NewRat(math.MaxInt64, 10)
	d2 := big.NewRat(1024, 10)
	d3 := big.NewRat(30000000000000000, 1)
	d2.Mul(d1,d3)
	fmt.Printf("d1:%v\n", d1)
	fmt.Printf("d2:%v\n", d2)
	fmt.Printf("d3:%v\n", d3)
	fmt.Println("hello world")
}
