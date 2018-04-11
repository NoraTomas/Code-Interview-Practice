public class SelectionSort {

    private int [] numlist = {4, 9, 7, 1, 3, 6, 5};

    public SelectionSort(){

    }

    private void selectionSort(){
        int min = 1000;

        for(int i = 0; i < numlist.length; i++){
            for (int j = i; j < numlist.length; j++){
                if(numlist[j] < min){
                    min = numlist[j];
                }

                int temp = numlist[i];
                numlist[i] = min;
                numlist[j] = temp;

                min = 1000;
            }
        }

        System.out.println(convertIntListToString(numlist));
    }

    private StringBuilder convertIntListToString(int [] someList){
        StringBuilder initial = new StringBuilder();

        for (int i=0; i < someList.length; i++){
            initial.append(Integer.toString(someList[i]));
        }

        return initial;
    }

    public static void main(String[] args) {
        SelectionSort selectionSort = new SelectionSort();
        selectionSort.selectionSort();
    }
}
