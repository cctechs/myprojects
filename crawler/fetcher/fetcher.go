package fetcher

import (
	"net/http"
	"golang.org/x/text/transform"
	"io/ioutil"
	"io"
	"golang.org/x/text/encoding"
	"bufio"
	"golang.org/x/net/html/charset"
	"fmt"
	"golang.org/x/text/encoding/unicode"
	"log"
	"time"
)

func determineEncoding(r io.Reader) encoding.Encoding{
	bytes, err := bufio.NewReader(r).Peek(1024)
	if err != nil{
		log.Printf("Fetch error:%v", err)
		return unicode.UTF8
	}
	e, _, _ := charset.DetermineEncoding(bytes, "")
	return e
}

var rateLimiter = time.Tick(10*time.Millisecond)

// 提取数据
func Fetch(url string)([]byte, error){

	<-rateLimiter

	resp, err := http.Get(url)
	if err != nil{
		return nil, err
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK{
		return nil, fmt.Errorf("wrong status code:%d", resp.StatusCode)
	}

	e := determineEncoding(resp.Body)

	utfReader := transform.NewReader(resp.Body,
		e.NewDecoder())

	return ioutil.ReadAll(utfReader)
}