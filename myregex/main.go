package main

import (
	"os"
	"io/ioutil"
	"fmt"
	"regexp"
)

const data  = `
function test001(a in number, --123
         b in number) -- 456
         return integer;


function test002(a in number, --123
         b in number) -- 456
         return integer;    
`

const reVarFunc = "function[\\s]+([\\w]+)\\(([^\\)]+\\))[\\s\\S]+?return[\\s]+([\\w]+);"

var(
	reFunc *regexp.Regexp
)

func Div(a, b int32) float64  {
	return float64(a/b)
}

func init(){
	reFunc = regexp.MustCompile(reVarFunc)
}

func main(){
	ip, err := os.Open("test.pck")
	if err != nil{
		panic(err)
	}
	bs, err := ioutil.ReadAll(ip)
	if err != nil{
		panic(err)
	}
	//fmt.Println(string(bs))
	arr := reFunc.FindAllStringSubmatch(string(bs), -1)
	for _, m := range arr{
		fmt.Println()
		for k, v := range m{
			fmt.Printf("%v->%v\n", k, v)
		}
	}
	//buf := bytes.NewBuffer(bs)
	//fmt.Println(buf.String())
	//str := buf.String()
	//fmt.Println(string(bs))
	//str := string(bs)
	//arr := strings.Split(str,";")
	//fmt.Println(arr)
	//for _, s := range arr{
	//	result := reFunc.FindAllStringSubmatch(s, -1)
	//	for _, m := range result{
	//		for k, v := range m{
	//			fmt.Printf("%v-%v\n", k, v)
	//		}
	//	}
	//}
}
