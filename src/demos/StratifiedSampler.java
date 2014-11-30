package demos;

import java.util.ArrayList;

import com.nicktikhonov.morsel.stratified_sampler.Field;
import com.nicktikhonov.morsel.stratified_sampler.Vector;

public class StratifiedSampler {

	public static void main(String[] args){
        int x1 = Integer.parseInt(args[0]);
        int y1 = Integer.parseInt(args[1]);

        int x2 = Integer.parseInt(args[2]);
        int y2 = Integer.parseInt(args[3]);

        int x3 = Integer.parseInt(args[4]);
        int y3 = Integer.parseInt(args[5]);

        int x4 = Integer.parseInt(args[6]);
        int y4 = Integer.parseInt(args[7]);

        int numDivisions = Integer.parseInt(args[8]);
        int numSamples = Integer.parseInt(args[9]);

		Field demo = new Field(
					new Vector(x1, y1),
					new Vector(x2, y2),
					new Vector(x3, y3),
					new Vector(x4, y4)
				);

		demo.generateRects(numDivisions, numSamples); //Generate a field with 2x2 strata grid

		ArrayList<Vector> samples = demo.getSamples();

        System.out.println("{ samples: [");

        for(int i = 0; i < samples.size(); i++){
		    System.out.print(samples.get(i).toString());
		    if(i + 1 < samples.size())
		        System.out.print(", ");
        }

		System.out.println(" ]}");
	}

}
