import java.util.ArrayList;
import java.util.Random;

public class SampleArea {

	private SampleVector v1, v2, v3, v4;
	private ArrayList<SampleVector> samplePoints;

	public SampleArea(SampleVector v1, SampleVector v2, SampleVector v3, SampleVector v4){
		samplePoints = new ArrayList<SampleVector>();

		this.v1 = v1;
		this.v2 = v2;
		this.v3 = v3;
		this.v4 = v4;

		generateSamples(1);
	}

	public void generateSamples(int numSamples){
		SampleTriangle t1 = new SampleTriangle(v1, SampleVector.sub(v2, v1), SampleVector.sub(v4, v1));
		SampleTriangle t2 = new SampleTriangle(v3, SampleVector.sub(v2, v3), SampleVector.sub(v4, v3));

		Random r = new Random();
		for(int i = 0; i < numSamples; i++){
			if(r.nextBoolean()){
				samplePoints.add(t1.getPointInside(r));
			}else{
				samplePoints.add(t2.getPointInside(r));
			}
		}
	}

}
