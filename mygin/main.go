package main

import (
	"database/sql"
	"fmt"
	"github.com/gin-gonic/gin"
	_ "github.com/go-sql-driver/mysql"
	"io"
	"log"
	"net/http"
	"os"
)

type MyData struct {
	Email string `form:"email"`
	Name  string `form:"name"`
}

type QueryResult []map[string]interface{}

func TestMyDb() {
	//db, err := sql.Open("mysql", "root:@tcp(127.0.0.1:3306):wubo123456@/test123")
	db, err := sql.Open("mysql", "weber:123qwe@/myshop")
	defer db.Close()

	err = db.Ping()
	if err != nil {
		panic(err)
	}

	stmtOut, err := db.Query("select * from t_product")
	if err != nil {
		panic(err)
	}
	defer stmtOut.Close()

	columns, err := stmtOut.Columns()
	if err != nil {
		panic(err)
	}

	fmt.Println(columns)

	values := make([]sql.RawBytes, len(columns))
	scanArgs := make([]interface{}, len(values))
	for i := range values {
		scanArgs[i] = &values[i]
	}

	result := make([]map[string]interface{}, 0)

	for stmtOut.Next() {
		err = stmtOut.Scan(scanArgs...)
		if err != nil {
			panic(err.Error())
		}
		mapData := make(map[string]interface{})
		var value string
		for i, col := range values {
			if col == nil {
				value = "NULL"
			} else {
				value = string(col)
			}
			//fmt.Println(columns[i], value)
			mapData[columns[i]] = value
		}
		result = append(result, mapData)
	}
	fmt.Println(result)

}

func main() {
	{
		TestMyDb()
		return
	}
	/*
		r := gin.Default()
		r.LoadHTMLGlob("views/*")
		r.Static("static", "./static")
		r.GET("/ping", func(c *gin.Context) {
			c.HTML(http.StatusOK, "home.html", gin.H{
				"title": "posts",
			})
		})
		r.Run()
	*/

	r := gin.Default()

	r.LoadHTMLGlob("views/*")
	r.Static("static", "./static")

	r.GET("/index", func(c *gin.Context) {
		c.HTML(http.StatusOK, "home.html", nil)
	})

	r.GET("/login/:name", func(c *gin.Context) {
		name := c.Param("name")
		c.String(http.StatusOK, "Hello %s\n", name)
	})

	r.GET("/search", func(c *gin.Context) {
		text := c.Query("keyvalue")
		fmt.Println(text)
		c.JSON(http.StatusOK, gin.H{
			"result": "ok",
		})
	})

	r.POST("/form/email", func(c *gin.Context) {
		contentType := c.Request.Header.Get("Content-Type")
		var data MyData
		if err := c.ShouldBind(&data); err != nil {
			log.Fatal(err)
			return
		}
		fmt.Println(data)
		fmt.Println(contentType)
		//email := c.PostForm("email")
		//name := c.PostForm("name")
		//fmt.Println(email, name)
		c.JSON(http.StatusOK, gin.H{
			"status": "ok",
			"email":  data.Email,
			"name":   data.Name,
		})
	})

	r.POST("/form/file", func(c *gin.Context) {
		contentType := c.Request.Header.Get("Content-Type")
		fmt.Println(contentType)

		file, header, err := c.Request.FormFile("upload")
		if err != nil {
			c.String(http.StatusBadRequest, "Bad Request")
			return
		}

		if header.Size > 10*1024*1024 {
			c.String(http.StatusOK, "too big")
			return
		}

		fileName := header.Filename
		dir := "upload"
		fmt.Println(fileName)
		curPath := dir + "//" + fileName
		out, err := os.Create(curPath)
		if err != nil {
			log.Fatal(err)
		}
		defer out.Close()

		_, err = io.Copy(out, file)
		if err != nil {
			log.Fatal(err)
		}
		c.String(http.StatusCreated, "upload successful")
	})

	r.POST("/form/files", func(c *gin.Context) {
		contentType := c.Request.Header.Get("Content-Type")
		fmt.Println(contentType)

		err := c.Request.ParseMultipartForm(200000)
		if err != nil {
			log.Fatal(err)
		}

		formdata := c.Request.MultipartForm
		files := formdata.File["upload"]
		for i, _ := range files {
			file, err := files[i].Open()
			defer file.Close()

			if err != nil {
				log.Fatal(err)
				continue
			}

			fileName := files[i].Filename

			dir := "upload"
			fmt.Println(fileName)
			curPath := dir + "//" + fileName
			out, err := os.Create(curPath)
			if err != nil {
				log.Fatal(err)
			}
			defer out.Close()

			_, err = io.Copy(out, file)
			if err != nil {
				log.Fatal(err)
			}
		}

		c.String(http.StatusCreated, "upload successful")
	})
	r.POST("/form_post", func(c *gin.Context) {
		message := c.PostForm("message")
		nick := c.DefaultPostForm("nick", "anonymous")
		c.JSON(http.StatusOK, gin.H{
			"status": gin.H{
				"status_code": http.StatusOK,
				"status":      "ok",
			},
			"message": message,
			"nick":    nick,
		})
	})

	r.Run(":1001")
}
