import os
import re
import json
import matplotlib.pyplot as plt




# 1) find your latest checkpoint folder
def printPlots(output_dir):
    
    # 2) build path to its trainer_state.json
    state_path = output_dir
    
    # 3) load the state and extract log history
    with open(state_path, "r") as f:
        state = json.load(f)
    history = state["log_history"]
    
    # 4) split out the metrics
    train_steps, train_loss = [], []
    eval_steps, eval_loss, eval_acc = [], [], []
    for rec in history:
        if "loss" in rec and "eval_loss" not in rec:
            train_steps.append(rec["step"])
            train_loss.append(rec["loss"])
        if "eval_loss" in rec:
            eval_steps.append(rec["step"])
            eval_loss.append(rec["eval_loss"])
            eval_acc.append(rec.get("eval_accuracy", None))
    
    # 5) plot with matplotlib
    plt.figure(figsize=(12,5))
    
    plt.subplot(1,2,1)
    plt.plot(train_steps, train_loss, label="Train Loss")
    plt.plot(eval_steps,  eval_loss,  label="Eval Loss")
    plt.xlabel("Step"); plt.ylabel("Loss")
    plt.title("Loss curves")
    plt.legend()
    
    plt.subplot(1,2,2)
    plt.plot(eval_steps, eval_acc, label="Eval Acc")
    plt.xlabel("Step"); plt.ylabel("Accuracy")
    plt.title("Validation Accuracy")
    plt.legend()
    
    plt.tight_layout()
    fig_path = "training_curves.png"
    plt.savefig(fig_path, dpi=300)
    print(f"Saved plot to {fig_path}")
    plt.show()

printPlots('trainer_state.json')