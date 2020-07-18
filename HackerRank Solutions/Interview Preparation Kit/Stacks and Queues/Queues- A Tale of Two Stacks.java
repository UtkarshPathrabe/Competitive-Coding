import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static class MyQueue<T> {

        private Stack stack1;
        private Stack stack2;

        public <T> MyQueue() {
            this.stack1 = new Stack<>();
            this.stack2 = new Stack<>();
        }

        public <T> void enqueue(T value) {
            this.stack1.push(value);
        }

        public <T> void dequeue() {
            if (this.stack2.isEmpty()) {
                while (!this.stack1.isEmpty()) {
                    this.stack2.push(this.stack1.pop());
                }
            }
            this.stack2.pop();
        }

        public <T> Object peek() {
            if (this.stack2.isEmpty()) {
                while (!this.stack1.isEmpty()) {
                    this.stack2.push(this.stack1.pop());
                }
            }
            return this.stack2.peek();
        }

    }

    public static void main(String[] args) {
        MyQueue<Integer> queue = new MyQueue<Integer>();

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        for (int i = 0; i < n; i++) {
            int operation = scan.nextInt();
            if (operation == 1) { // enqueue
              queue.enqueue(scan.nextInt());
            } else if (operation == 2) { // dequeue
              queue.dequeue();
            } else if (operation == 3) { // print/peek
              System.out.println(queue.peek());
            }
        }
        scan.close();
    }
}