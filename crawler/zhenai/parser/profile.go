package parser

import (
	"github.com/myprojects/crawler/engine"
	"regexp"
	"fmt"
)

const nameRe = `<a href="http://album.zhenai.com/u/1314495053" target="_blank">风中的蒲公英</a>`

const ageRe =`<td><span class="label">年龄：</span>([0-9]+)</td>`


func ParseProfile(contents []byte) engine.ParseResult{
	re, err := regexp.Compile(ageRe)
	if err != nil{
		panic(err)
	}
	fmt.Println(re.FindAll(contents, -1))
	return engine.ParseResult{}
}
