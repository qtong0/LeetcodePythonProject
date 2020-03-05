class MyCalendarThree(object):
    # Checkout Java Solution!
    pass


"""

class MyCalendarThree {
    private TreeMap<Integer, Integer> timeline = new TreeMap<>();

    public MyCalendarThree() {
        return;
    }
    
    public int book(int start, int end) {
        timeline.put(start, timeline.getOrDefault(start, 0)+1);
        timeline.put(end, timeline.getOrDefault(end, 0)-1);
        int ongoing = 0, k = 0;
        for (int v: timeline.values()) {
        	ongoing += v;
        	k = Math.max(k, ongoing);
        }
        return k;
    }
}

"""
