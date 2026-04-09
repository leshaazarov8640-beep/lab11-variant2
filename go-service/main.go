package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	// Простой эндпоинт для проверки связи и тестов производительности
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"status": "ok", "service": "go"})
	})

	// Логика обработки (Relay)
	r.POST("/process-user", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"message": "Data processed by Go backend"})
	})

	r.Run(":8080")
}
