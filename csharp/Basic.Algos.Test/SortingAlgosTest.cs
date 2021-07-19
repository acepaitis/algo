using Microsoft.VisualStudio.TestTools.UnitTesting;
using Basic.Algos;

namespace Basic.Algos.Test
{
  [TestClass]
  public class SortingAlgosTest
  {
    [TestMethod]
    public void Sorting_InsertionSort_SortOrder_Match()
    {
      var arr = new int[] { 56, 5, 1, 9, 3, 10, 2, 9, 7 };
      arr.InsertionSort();

      CollectionAssert.AreEqual(new int[] { 1, 2, 3, 5, 7, 9, 9, 10, 56 }, arr);
    }
  }
}
