package com.example.isaiah.elixr;

import android.content.Intent;
import android.nfc.cardemulation.CardEmulation;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.CardView;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        CardView card = findViewById(R.id.fitness_card);
        card.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent myIntent = new Intent(MainActivity.this, FitnessActivity.class);
                MainActivity.this.startActivity(myIntent);
                System.out.println("i touched the fitness card");
            }
        });
    }
}
