import java.util.ArrayList;

public class SampleField {

	private SampleVector corner1, corner2, corner3, corner4;
	ArrayList<SampleArea> subFields;

	public SampleField(SampleVector v1, SampleVector v2,SampleVector v3,SampleVector v4){
		this.corner1 = v1;
		this.corner2 = v2;
		this.corner3 = v3;
		this.corner4 = v4;
	}

	public void generateRects(int divisions){
		subFields = new ArrayList<SampleArea>();

		SampleVector horiz1 = SampleVector.sub(corner2, corner1);
		SampleVector horiz2 = SampleVector.sub(corner3, corner4);

		double step1 = horiz1.getLength()/divisions;
		double step2 = horiz2.getLength()/divisions;

		SampleVector[][] points = new SampleVector[divisions + 1][divisions + 1];


		for(int i = 0; i <= divisions; i++){
			SampleVector current1 = SampleVector.sum(corner1, SampleVector.scale(horiz1, i * step1));
			SampleVector current2 = SampleVector.sum(corner4, SampleVector.scale(horiz2, i * step2));

			SampleVector currentVertLine = SampleVector.sub(current2, current1);
			double currentStep = currentVertLine.getLength()/divisions;

			for(int j = 0; j <= divisions; j++){
				SampleVector pointPos = SampleVector.sum(current1, SampleVector.scale(currentVertLine, j * currentStep));
				points[i][j] = pointPos;
			}
		}

		for(int x = 0; x < divisions; x++){
			for(int y = 0; y < divisions; y++){
				subFields.add(new SampleArea(points[x][y], points[x + 1][y], points[x + 1][y + 1], points[x][y + 1]));
			}
		}
	}

}
