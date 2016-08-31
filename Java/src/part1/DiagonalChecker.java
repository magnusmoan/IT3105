package part1;

public class DiagonalChecker {

public static boolean diagonal_conflict(int row, int col, int[] columnList) {
		
		for(int currCol = 0; currCol < col; currCol++){
			int currRow = columnList[currCol];
			if( (currRow != row || currCol != col) && currRow != -1) {
				if ( Math.abs(currRow - row) == Math.abs(currCol - col) ) {
					return true;
				}
			}
		}
		
		return false;
	}
}
