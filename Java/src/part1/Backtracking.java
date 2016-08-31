package part1;

import java.util.HashSet;
import java.util.Scanner;

import part1.Board;

public class Backtracking {

	static int n;
	static int counter = 0;
	static long start;
	static long end;
	
	public static void main(String[] args) {
		
		Scanner user_input = new Scanner(System.in);
		
		String[] starting_positions_as_strings = user_input.nextLine().split(" ");
		
		user_input.close();
		
		int[] starting_positions = new int[starting_positions_as_strings.length];
		
		
		for(int i = 0; i < starting_positions_as_strings.length; i++) {
			starting_positions[i] = Integer.parseInt(starting_positions_as_strings[i]) - 1;
		}
		
		n = starting_positions.length;
		
		
		Board startingBoard = new Board(starting_positions);
		
		if(StartingPositionValidator.starting_position_valid(starting_positions)) {
			System.out.println("Valid starting position. Starting backtracking search for feasable solutions");
			start = System.currentTimeMillis();
			try_col(startingBoard);
			end = System.currentTimeMillis();
			System.out.print("Total time used: ");
			System.out.println((end - start) / 1000F);
			System.out.print("Number of solutions found: ");
			System.out.println(counter);
		} else {
			System.out.println("Invalid starting position.");
		}
		
	}
	
	
	private static void try_col(Board board) {
		
		int col = board.getCol();
		int[] colList = board.getColList();
		HashSet<Integer> rowsSet = board.getRowsSet();
		
		if (col == n) {
			counter++;
			System.out.println(board.toString());
		}
		
		if (rowsSet.size() == 0) {
			return;
		}

		for(int row : rowsSet) {
			if(!DiagonalChecker.diagonal_conflict(row, col, colList)) {
				int[] newColList = colList;
				newColList[col] = row;
				HashSet<Integer> newRowsSet = new HashSet<Integer>(rowsSet);
				newRowsSet.remove(row);
				
				try_col(new Board(col + 1, newColList, newRowsSet));
			}
		}
	}
}
