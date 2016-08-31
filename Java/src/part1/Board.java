package part1;

import java.util.Arrays;
import java.util.HashSet;

public class Board {

	int col = 0;
	int[] colList;
	HashSet<Integer> rowsSet;
	
	public Board(int[] colList) {
		this.colList = colList;
		this.rowsSet = new HashSet<Integer>();
		
		HashSet<Integer> tempSet = new HashSet<Integer>();
		
		for(int i = 0; i < colList.length; i++) {
			if (this.colList[i] >= 0) {
				tempSet.add(this.colList[i]);
				this.col++;
			}
			this.rowsSet.add(i);
		}
		this.rowsSet.removeAll(tempSet);
		
		
	}
	
	public Board(int col, int[] colList, HashSet<Integer> rowsSet) {
		this.col = col;
		this.colList = colList;
		this.rowsSet = rowsSet;
	}
	
	public int getCol() {
		return this.col;
	}
	
	public int[] getColList() {
		return this.colList;
	}

	public HashSet<Integer> getRowsSet() {
		return this.rowsSet;
	}
	
	public String toString() {
		int[] printList = new int[this.colList.length];
		for(int i = 0; i < this.colList.length; i++) {
			printList[i] = this.colList[i] + 1;
		}
		return Arrays.toString(printList);
	}
}
