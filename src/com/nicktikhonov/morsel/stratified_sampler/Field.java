package com.nicktikhonov.morsel.stratified_sampler;

import java.util.ArrayList;

public class Field {

	private Vector corner1, corner2, corner3, corner4;
	private ArrayList<Area> subFields;

	public Field(Vector v1, Vector v2,Vector v3,Vector v4){
		this.corner1 = v1;
		this.corner2 = v2;
		this.corner3 = v3;
		this.corner4 = v4;
	}

	public void generateRects(int lengthDivisions, int numSamples){
		subFields = new ArrayList<Area>();

		Vector horiz1 = Vector.sub(corner2, corner1);
		Vector horiz2 = Vector.sub(corner3, corner4);

		double step1 = horiz1.getLength()/lengthDivisions;
		double step2 = horiz2.getLength()/lengthDivisions;

		Vector[][] points = new Vector[lengthDivisions + 1][lengthDivisions + 1];


		for(int i = 0; i <= lengthDivisions; i++){
			Vector current1 = Vector.sum(corner1, Vector.scale(horiz1, i * step1));
			Vector current2 = Vector.sum(corner4, Vector.scale(horiz2, i * step2));

			Vector currentVertLine = Vector.sub(current2, current1);
			double currentStep = currentVertLine.getLength()/lengthDivisions;

			for(int j = 0; j <= lengthDivisions; j++){
				Vector pointPos = Vector.sum(current1, Vector.scale(currentVertLine, j * currentStep));
				points[i][j] = pointPos;
			}
		}

		for(int x = 0; x < lengthDivisions; x++){
			for(int y = 0; y < lengthDivisions; y++){
				subFields.add(new Area(points[x][y], points[x + 1][y], points[x + 1][y + 1], points[x][y + 1], numSamples));
			}
		}
	}
	
	public ArrayList<Vector> getSamples(){
		ArrayList<Vector> samples = new ArrayList<Vector>();
		for(Area subField: subFields){
			samples.addAll(subField.getSamples());
		}
		
		return samples;
	}

}
