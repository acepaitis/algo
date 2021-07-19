using System;

namespace Basic.Algos
{
  public static class SortingAlgos
  {
    public static void InsertionSort(this int[] arrayToSort)
    {
      for (int index = 1; index < arrayToSort.Length; index++)
      {
        var key = arrayToSort[index];
        var innerIndex = index - 1;
        while (innerIndex > -1 && arrayToSort[innerIndex] > key)
        {
          arrayToSort[innerIndex + 1] = arrayToSort[innerIndex];
          innerIndex -= 1;
        }

        arrayToSort[innerIndex + 1] = key;
      }
    }
  }
}
