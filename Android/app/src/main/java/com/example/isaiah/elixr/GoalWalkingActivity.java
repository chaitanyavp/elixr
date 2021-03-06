package com.example.isaiah.elixr;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class GoalWalkingActivity extends AppCompatActivity implements SensorEventListener {


    private TextView stepCountText;
    private TextView goalPhraseText;
    private TextView calorieCountText;
    private TextView kilometerText;

    private SensorManager sensorManager;
    private Sensor stepSensor;

    private boolean isSensorPresent = false;

    private static final double caloriesPerKilometer = 150.0/3.2;
    private static final double kilometersPerStep = 0.44 * 1.60934/1000;

    private int goalStepCount;
    private int stepCount;
    private int lastDoubleQuartile = 0;
    private int stepsBetweenAPICalls = 50;

    private String userID = "50fa056a-d0e2-4241-aa39-340538634033_39ff2dc1-e430-4498-a645-155e83e05403";

    // Firebase things
    private DatabaseReference mDatabase;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_goal_walking);
        this.goalStepCount = 10000;

        stepCountText = findViewById(R.id.step_count_text);
        goalPhraseText = findViewById(R.id.step_goal_text);
        calorieCountText = findViewById(R.id.calories_text);
        kilometerText = findViewById(R.id.distance_travelled_text);

        sensorManager = (SensorManager) this.getSystemService(Context.SENSOR_SERVICE);
        if(sensorManager.getDefaultSensor(Sensor.TYPE_STEP_COUNTER) != null) {
            stepSensor = sensorManager.getDefaultSensor(Sensor.TYPE_STEP_COUNTER);
            isSensorPresent = true;
        } else {
            isSensorPresent = false;
        }

        mDatabase = FirebaseDatabase.getInstance().getReference();
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        System.out.println("the current pedometer value is: " + event.values[0]);
        this.stepCount = (int)event.values[0];

        stepCountText.setText(String.valueOf(stepCount));
        goalPhraseText.setText("of " + goalStepCount + " steps");
        kilometerText.setText(((int)(10*kilometersPerStep * this.stepCount))/10.0+"km");
        calorieCountText.setText((int)(caloriesPerKilometer * kilometersPerStep * stepCount) + "cal");

        int currentDoubleQuartile = this.stepCount / stepsBetweenAPICalls;

        if(currentDoubleQuartile > this.lastDoubleQuartile) {
            lastDoubleQuartile = currentDoubleQuartile;
            System.out.println("exceeded double quartile");
            this.writeToDatabase();
        }
    }

    public void writeToDatabase() {

        try {
            mDatabase.child(userID).child("steps").setValue(stepCount);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }

    @Override
    protected void onPause() {
        super.onPause();
        if(isSensorPresent)
        {
            sensorManager.unregisterListener(this);
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        if(isSensorPresent) {
            sensorManager.registerListener(this, stepSensor, SensorManager.SENSOR_DELAY_NORMAL);
        }
    }
}
