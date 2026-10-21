class ListNode {
    int value;
    ListNode next;

    public ListNode(int value) {
        this(value, null);
    }

    public ListNode(int value, ListNode next) {
        this.value = value;
        this.next = next;
    }
}

class LinkedList {
    private ListNode head;
    private ListNode tail;

    public LinkedList() {
        this.head = new ListNode(-1);
        this.tail = this.head;
    }

    public int get(int index) {
        ListNode current = this.head.next;
        int i = 0; 
        while (current != null) {
            if (i == index) {
                return current.value;
            }
            i ++;
            current = current.next;
        }
        return -1;
    }

    public void insertHead(int val) {
        ListNode newNode = new ListNode(val);
        newNode.next = this.head.next;
        head.next = newNode;
        if (newNode.next == null) {
            tail = newNode;
        }
    }

    public void insertTail(int val) {
        this.tail.next = new ListNode(val);
        this.tail = this.tail.next;
    }

    public boolean remove(int index) {
        ListNode current = this.head;
        int i = 0;
        while (i < index && current != null) {
            i ++;
            current = current.next;
        }

        if (current != null && current.next != null) {
            if (current.next == this.tail) {
                this.tail = current;
            }
            current.next = current.next.next;
            return true;
        }
        return false;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> result = new ArrayList<>();
        ListNode current = this.head.next;
        while (current != null) {
            result.add(current.value);
            current = current.next;
        }
        return result;
    }
}
