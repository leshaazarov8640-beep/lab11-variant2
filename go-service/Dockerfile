# Stage 1: Build
FROM golang:1.23-alpine AS builder
WORKDIR /app
COPY . .
RUN go mod tidy && go mod download
RUN go build -o main .

# Stage 2: Final image
FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/main .
EXPOSE 8080
CMD ["./main"]