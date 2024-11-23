class MyStack() {

    val q1: Queue<Int> = LinkedList<Int>()
    val q2: Queue<Int> = LinkedList<Int>()

    fun push(x: Int) {
        q1.add(x)
        while (!q2.isEmpty())
            q1.add(q2.poll())
        while (!q1.isEmpty())
            q2.add(q1.poll())
    }

    fun pop(): Int {
        return q2.poll()
    }

    fun top(): Int {
        return q2.peek()
    }

    fun empty(): Boolean {
        return q2.isEmpty()
    }

}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */