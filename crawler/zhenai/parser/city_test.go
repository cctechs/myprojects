package parser

import (
	"testing"
)

func TestParseCity(t *testing.T) {
	/*
	engine.Run(engine.Request{
		Url:`http://album.zhenai.com/u/1045553884`,
		ParserFunc:ParseProfile,
	})
	*/

	ParseProfile([]byte(`<td><span class="label">年龄：</span>35岁</td>`), "")
	ParseProfile([]byte(`<td><span class="label">身高：</span>165CM</td>`), "")
	ParseProfile([]byte(`<td><span class="label">月收入：</span>20001-50000元</td>`), "")
	ParseProfile([]byte(`<td><span class="label">婚况：</span>未婚</td>`), "")
	ParseProfile([]byte(`<td><span class="label">学历：</span>博士</td>`), "")
	ParseProfile([]byte(`<td><span class="label">籍贯：</span>北京昌平区</td>`), "")
}
