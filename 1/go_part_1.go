package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	// init vars
	file_name := "./1/input.txt"

	var l int
	var r int

	sum := 0

	// init file reader
	f, err := os.Open(file_name)
	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		// do something with a line
		word := scanner.Text()
		//fmt.Printf("line: %s\n", word)

		li := 0
		ri := len(word) - 1

		for li < len(word) {
			l, err = strconv.Atoi(string(word[li]))
			if err == nil {
				break
			}
			li = li + 1
		}

		for ri >= 0 {
			r, err = strconv.Atoi(string(word[ri]))
			if err == nil {
				break
			}
			ri = ri - 1
		}

		ret := (l * 10) + r
		fmt.Println(ret)

		sum = sum + ret

	}

	fmt.Println(sum)

}
