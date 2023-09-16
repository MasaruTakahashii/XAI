
package main

import (
	"context"
	"crypto/sha256"
	"fmt"
	"time"
)

func main() {
	ctx := context.Background()

	data := make([]byte, 64<<20)
	for i := range data {
		data[i] = byte(i)
	}
	benchSHA256(ctx, data)
}

func benchSHA256(ctx context.Context, data []byte) {
	fmt.Println("SHA256:")
	buf := make([]byte, 32)

	const (
		iter      = 1e10
		chunkSize = 1 << 12
	)
	start := time.Now()
	h := sha256.New()

	for off := 0; off < len(data); off += chunkSize {
		l := chunkSize
		if rem := len(data) - off; rem < l {
			l = rem
		}
		if n, err := h.Write(data[off : off+l]); err != nil {
			panic(err)
		} else if n != l {
			panic("short write")
		}
		select {
		case <-ctx.Done():
			return
		default:
		}
	}

	for iter > 0 {
		if _, err := h.Write(buf); err != nil {
			panic(err)
		}
		select {
		case <-ctx.Done():
			return
		default:
		}
		iter--
	}
	end := time.Now()
	dur := end.Sub(start)
	perOp := dur / (1e7 + (iter-1)/chunkSize)
	fmt.Printf("  %.1fs, %s/op\n", dur.Seconds(), perOp)
}
