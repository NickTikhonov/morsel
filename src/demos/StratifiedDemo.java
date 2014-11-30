package demos;

import java.util.ArrayList;

import com.nicktikhonov.morsel.stratified_sampler.Field;
import com.nicktikhonov.morsel.stratified_sampler.Vector;

public class StratifiedDemo {

	public static void main(String[] args){
		Field demo = new Field(
					new Vector(0.0, 0.0),
					new Vector(10.0, 0.0),
					new Vector(10.0, 10.0),
					new Vector(0.0, 10.0)
				);
		
		demo.generateRects(2,1); //Generate a field with 2x2 strata grid
		
		ArrayList<Vector> samples = demo.getSamples();
		
		for(int x = 0; x < 2; x++){
			for(int y = 0; y < 2; y++){
				System.out.print(samples.get(x * 2  + y).toString() + " ");
			}
			System.out.println();
		}
	}
	
}
