package part1;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

import part1.DiagonalChecker;

public class StartingPositionValidator {

	private static boolean duplicates_in_array(int[] arr) {
		Set<Integer> arr_set = new HashSet<Integer>();
		for(int col : arr) {
			if (arr_set.contains(col)) {
				return true;
			} else {
				arr_set.add(col);
			}
		}
		return false;
	}
	
	private static int[] remove_all_negative(int[] arr) {
		ArrayList<Integer> without_negative = new ArrayList<Integer>();
		for(int col : arr) {
			if (col >= 0) {
				without_negative.add(col);
			}
		}
		
		int[] result = new int[without_negative.size()];
		
		for(int i = 0; i < result.length; i++) {
			result[i] = without_negative.get(i);
		}
		
		return result;
	}
	
	public static boolean starting_position_valid(int[] arr) {
		
		int[] without_neg = remove_all_negative(arr);
		
		if (duplicates_in_array(without_neg)) {
			return false;
		}
		
		for (int col = 0; col < without_neg.length; col++) {
			if (DiagonalChecker.diagonal_conflict(without_neg[col], col, without_neg)) {
				return false;
			}
		}
		return true;
	}

}
