class DynamicArray {
    private int[] arr;
    private int length;
    private int capacity;

    public DynamicArray(int capacity) {
       this.capacity = capacity;
       this.length = 0;
       this.arr = new int[this.capacity]; 
    }

    public int get(int i) {
        return this.arr[i];
    }

    public void set(int i, int n) {
        this.arr[i] = n;
    }

    public void pushback(int n) {
        if (this.length == this.capacity) {
            this.resize();
        }
        this.arr[length] = n;
        this.length ++;
    }

    public int popback() {
        if (this.length > 0) {
            this.length --;
        }
        return this.arr[length];
    }

    private void resize() {
        this.capacity *= 2;
        int[] newArr = new int[capacity];
        for (int i = 0; i < this.length; i ++) {
            newArr[i] = this.arr[i];
        }
        this.arr = newArr;
    }

    public int getSize() {
        return this.length;

    }

    public int getCapacity() {
        return this.capacity;
    }
}
