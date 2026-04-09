module go-service

go 1.23

require (
	github.com/gin-gonic/gin v1.9.1
	github.com/go-playground/validator/v10 v10.14.0
)

replace (
	github.com/go-playground/validator/v10 => github.com/go-playground/validator/v10 v10.14.0
	golang.org/x/net => golang.org/x/net v0.10.0
)