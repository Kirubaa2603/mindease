import React, { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Select, SelectItem } from "@/components/ui/select";
import { Tabs, Tab } from "@/components/ui/tabs";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { format } from "date-fns";

const motivationQuotes = [
  "You are capable of amazing things! 💪",
  "Believe in yourself, and magic will happen! ✨",
  "Small progress is still progress! 🌱",
  "You are stronger than you think! 🔥",
  "Every day is a fresh start! 🌅",
  "Success is the sum of small efforts! 🎯",
  "Keep pushing forward, you're doing great! 🚀",
  "Your hard work will pay off! 🌟",
  "Don't give up, you've got this! 🏆",
  "Stay positive and good things will happen! 😊",
];

const anxietyReliefPrompts = [
  "Take a deep breath in... and out. 🌬️",
  "You are safe and in control. 🛡️",
  "This feeling will pass. Just breathe. 💖",
  "Close your eyes and count to 10 slowly. 🔢",
  "Visualize a peaceful place. 🏞️",
  "Focus on what you can control. 🏆",
  "Drink some water and relax. 💧",
  "Stretch your arms and release tension. 🙆",
  "Listen to calming music. 🎵",
  "Write down what's on your mind. ✍️",
];

const studyTips = [
  "Use the Feynman Technique to understand better! 📖",
  "Break your study time into 25-minute Pomodoro sessions! ⏳",
  "Teach what you learn to someone else. 🗣️",
  "Take regular breaks to stay fresh! ☕",
  "Use flashcards for memorization. 🎴",
  "Create a study plan and stick to it! 📅",
  "Stay hydrated and eat brain-boosting foods! 🥑",
  "Rewrite notes in your own words for better retention! ✍️",
  "Practice active recall—test yourself often! 🎯",
  "Find a quiet place with minimal distractions. 🔇",
];

const selfCareTips = [
  "Stretch your shoulders; release that tension. 🙆‍♂️",
  "Blink often and rest your eyes from screens. 👀",
  "Take deep breaths and relax. 🌬️",
  "Listen to calming music while studying. 🎵",
  "Drink water and stay hydrated. 💦",
  "Take short walks to refresh your mind. 🚶",
  "Avoid burnout by scheduling breaks. ☕",
  "Write positive affirmations about yourself. ✍️",
  "Get enough sleep for better focus. 😴",
  "Stay connected with friends for support. 🤝",
];

const feelingsPrompts = {
  happy: "Enjoy your happiness and spread the joy! 😊",
  sad: "It's okay to feel sad. You're not alone. 💙",
  stressed: "Take a deep breath; you've got this! 🌿",
  excited: "Embrace the excitement and keep going! 🎉",
  anxious: "Remember, you are safe and in control. 🛡️",
};

const studyDurations = ["5 minutes", "10 minutes", "25 minutes", "1 hour"];
const breakDurations = ["5 minutes", "10 minutes"];

export default function MindeaseApp() {
  const [selectedFeeling, setSelectedFeeling] = useState("");
  const [feelingPrompt, setFeelingPrompt] = useState("");
  const [affirmation, setAffirmation] = useState("");

  useEffect(() => {
    setAffirmation("You are doing great! Keep going! 🌟");
  }, []);

  return (
    <div className="p-6 bg-orange-50 min-h-screen text-brown-800">
      <h1 className="text-3xl font-bold">🌿 Welcome to MindEase Tools</h1>
      
      <Tabs>
        <Tab title="Motivation">  
          <Card>
            <CardContent>
              <p>✨ Need a boost?</p>
              <Button onClick={() => alert(motivationQuotes[Math.floor(Math.random() * motivationQuotes.length)])}>Inspire Me!</Button>
            </CardContent>
          </Card>
          <Card>
            <CardContent>
              <p>😌 Feeling anxious?</p>
              <Button onClick={() => alert(anxietyReliefPrompts[Math.floor(Math.random() * anxietyReliefPrompts.length)])}>Anxiety Relief</Button>
            </CardContent>
          </Card>
        </Tab>

        <Tab title="Study Tips">
          <Card>
            <CardContent>{studyTips[Math.floor(Math.random() * studyTips.length)]}</CardContent>
          </Card>
        </Tab>

        <Tab title="Self-Care">
          <Card>
            <CardContent>{selfCareTips[Math.floor(Math.random() * selfCareTips.length)]}</CardContent>
          </Card>
        </Tab>
      </Tabs>

      <h2 className="text-2xl mt-6">How do you feel today? 🧡</h2>
      <Select onValueChange={(value) => { setSelectedFeeling(value); setFeelingPrompt(feelingsPrompts[value]); }}>
        {Object.keys(feelingsPrompts).map((feeling) => (
          <SelectItem key={feeling} value={feeling}>{feeling}</SelectItem>
        ))}
      </Select>
      <p className="mt-4">{feelingPrompt}</p>
      
      <h2 className="text-2xl mt-6">📅 Daily Affirmation</h2>
      <p>{affirmation}</p>
    </div>
  );
}
