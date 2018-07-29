package engine

// 解析结果
type ParseResult struct {
	Requests []Request
	Items    []interface{}
}

type Request struct {
	Url        string
	ParserFunc func([]byte) ParseResult // 解析url
}

func NilParser([]byte) ParseResult {
	return ParseResult{}
}
