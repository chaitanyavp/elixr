package com.example.isaiah.elixr;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.CardView;
import android.view.View;

public class BudgetingActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bud);

        CardView walkingCard = findViewById(R.id.walking_card);

        walkingCard.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent myIntent = new Intent(BudgetingActivity.this, GoalWalkingActivity.class);
                BudgetingActivity.this.startActivity(myIntent);
            }
        });
    }
}
