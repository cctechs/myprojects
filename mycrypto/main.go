package main

import (
	"fmt"
	"github.com/ethereum/go-ethereum/crypto"
	"crypto/sha1"
	"io"
	"crypto/sha256"
	"crypto/sha512"
)

func MyHash(){
	hasher := sha1.New()
	io.WriteString(hasher, "test001")
	b := []byte{}

	fmt.Printf("Result:%x\n", hasher.Sum(b))
	fmt.Printf("Result:%x\n", hasher.Sum(b))
}

func MyHash256(str string)  {
	hasher := sha256.New()
	hasher.Write([]byte(str))

	b := []byte{}
	res := hasher.Sum(b)
	fmt.Printf("len:%v, val:%d\n", len(res), res)
	fmt.Printf("Result:%x\n", hasher.Sum(b))
	fmt.Printf("Result:%x\n", hasher.Sum(b))
	fmt.Printf("%v\n", b)
}

func MyHash512(str string)  {
	hasher := sha512.New()
	hasher.Write([]byte(str))

	b := []byte{}
	res := hasher.Sum(b)
	fmt.Printf("len:%v, val:%d\n", len(res), res)
	fmt.Printf("Result:%x\n", hasher.Sum(b))
	fmt.Printf("Result:%x\n", hasher.Sum(b))
	fmt.Printf("%v\n", b)
}

func main()  {
	data := make([]byte, 32)
	for i := 0; i < 32; i++{
		data[i] = 'a'
	}
	pk, err := crypto.ToECDSA(data)
	fmt.Println(pk.PublicKey.X)
	fmt.Println(pk.PublicKey.Y)
	fmt.Println(pk.D)
	fmt.Println(err)
	fmt.Println("hello world")
	MyHash()
	fmt.Println("myhash256")
	MyHash256("123456")
	MyHash256("123455")
	fmt.Println("myhash512")
	MyHash512("123456")
	MyHash512("123455")
}