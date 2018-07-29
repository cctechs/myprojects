package parser

import (
	"github.com/myprojects/crawler/engine"
	"regexp"
	"github.com/myprojects/crawler/model"
	"strconv"
)

const ageRe =`<td><span class="label">年龄：</span>([0-9]+)岁</td>`
const heightRe  = `<td><span class="label">身高：</span>([0-9]+)CM</td>`
const IncomeRe = `<td><span class="label">月收入：</span>([\d]+-[\d]+)元</td>`
const marrRe  = `<td><span class="label">婚况：</span>([^<]+)</td>`
const enducationRe  = `<td><span class="label">学历：</span>([^<]+)</td>`
const hukouRe  = `<td><span class="label">籍贯：</span>([^>]+)</td>`

var(
	reAge *regexp.Regexp
	reHeight * regexp.Regexp
	reIncome* regexp.Regexp
	reMarriage* regexp.Regexp
	reEnducation* regexp.Regexp
	reHukou*regexp.Regexp
)

func init(){
	reAge = regexp.MustCompile(ageRe)
	reHeight = regexp.MustCompile(heightRe)
	reIncome = regexp.MustCompile(IncomeRe)
	reMarriage = regexp.MustCompile(marrRe)
	reEnducation = regexp.MustCompile(enducationRe)
	reHukou = regexp.MustCompile(hukouRe)
}

func extractString(re *regexp.Regexp, contents []byte) string{
	matchs := re.FindSubmatch(contents)
	if len(matchs) > 1{
		//fmt.Println(string(matchs[1]))
		return string(matchs[1])
	}
	return ""
}

func extractInt(re* regexp.Regexp, contents []byte) int{
	matchs := re.FindSubmatch(contents)
	if len(matchs) > 1{
		//fmt.Println(string(matchs[1]))
		age, _ := strconv.Atoi(string(matchs[1]))
		return age
	}
	return -1
}

func ParseProfile(contents []byte, name string) engine.ParseResult{
	profile := model.Profile{}
	profile.Name = name
	profile.Age = extractInt(reAge, contents)
	profile.Height = extractInt(reHeight, contents)
	profile.Income = extractString(reIncome, contents)
	profile.Marriage = extractString(reMarriage, contents)
	profile.Education = extractString(reEnducation, contents)
	profile.HuKou = extractString(reHukou, contents)

	result := engine.ParseResult{}
	result.Items = append(result.Items, profile)

	return result
}
