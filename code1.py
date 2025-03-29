import React, { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Select, SelectItem } from "@/components/ui/select";

const motivationPrompts = [
  "Believe in yourself! You are stronger than you think.",
  "Every day is a new opportunity to grow.",
  "You are capable of achieving great things.",
  "Keep pushing forward, success is near!",
  "Hard times don’t last, strong people do.",
  "Take one step at a time, progress is still progress.",
  "Trust yourself and your abilities.",
  "You have the power to turn things around.",
  "Mistakes are proof that you are trying.",
  "Dream big, work hard, and make it happen."
];

const anxietyReliefPrompts = [
  "Take a deep breath, inhale for 4 seconds, hold for 7, exhale for 8.",
  "Write down what's bothering you, then let it go.",
  "Close your eyes and picture a peaceful place.",
  "Stretch your body to release tension.",
  "Listen to calming music or nature sounds.",
  "Try mindfulness – focus on the present moment.",
  "Drink a warm cup of tea and relax.",
  "Speak kind words to yourself.",
  "Move your body – go for a short walk.",
  "You are safe. Everything will be okay."
];

const studyTips = [
  "Use the Feynman technique to simplify concepts.",
  "Break study sessions into short, focused intervals.",
  "Teach someone else what you’ve learned.",
  "Make mind maps for better visualization.",
  "Practice active recall instead of passive reading.",
  "Stay hydrated and take breaks.",
  "Use flashcards for memorization.",
  "Change study locations to improve focus.",
  "Get enough sleep – your brain needs rest!",
  "Write summaries in your own words."
];

const selfCareTips = [
  "Take a short break and stretch your body.",
  "Breathe deeply – inhale positivity, exhale stress.",
  "Drink water, stay hydrated!",
  "Listen to your favorite relaxing music.",
  "Close your eyes and take 10 deep breaths.",
  "Write down 3 things you are grateful for.",
  "Give yourself permission to rest.",
  "Smile at yourself in the mirror – you got this!",
  "Read something inspiring.",
  "Step outside for a breath of fresh air."
];

const emotions = {
  Happy: "Keep spreading positivity and light! 🌞",
  Sad: "It's okay to feel this way. You are loved. 💙",
  Stressed: "Take a deep breath. You’re doing your best! 🌿",
  Motivated: "Keep that energy up! You're unstoppable! 🚀",
  Tired: "Rest is productive too. Take it easy. 🌙"
};

const MindEase = () => {
  const [selectedTab, setSelectedTab] = useState("Motivation");
  const [message, setMessage] = useState("");
  const [selectedEmotion, setSelectedEmotion] = useState("");
  const [studySubjects, setStudySubjects] = useState([]);
  const [timer, setTimer] = useState(0);

  const getRandomPrompt = (list) => list[Math.floor(Math.random() * list.length)];

  return (
    <div className="p-6 bg-[#F8F9FA] min-h-screen flex flex-col items-center text-gray-800">
      <h1 className="text-3xl font-bold">🌿 Welcome to MindEase Tools</h1>

      <div className="flex space-x-4 my-4">
        {["Motivation", "Study Tips", "Self-Care"].map((tab) => (
          <button
            key={tab}
            onClick={() => setSelectedTab(tab)}
            className={`px-4 py-2 rounded-lg ${selectedTab === tab ? "bg-blue-500 text-white" : "bg-gray-300"}`}
          >
            {tab}
          </button>
        ))}
      </div>

      <Card className="w-96 p-4 shadow-md bg-white">
        <CardContent>
          {selectedTab === "Motivation" && (
            <>
              <h2 className="text-lg font-semibold">✨ Need a boost?</h2>
              <Button onClick={() => setMessage(getRandomPrompt(motivationPrompts))}>Inspire Me!</Button>
              <h2 className="text-lg font-semibold mt-4">😊 Feeling anxious?</h2>
              <Button onClick={() => setMessage(getRandomPrompt(anxietyReliefPrompts))}>Anxiety Relief</Button>
            </>
          )}
          {selectedTab === "Study Tips" && (
            <Button onClick={() => setMessage(getRandomPrompt(studyTips))}>Get Study Tip</Button>
          )}
          {selectedTab === "Self-Care" && (
            <Button onClick={() => setMessage(getRandomPrompt(selfCareTips))}>Get Self-Care Tip</Button>
          )}
          {message && <p className="mt-4 text-blue-700">{message}</p>}
        </CardContent>
      </Card>

      <div className="my-6">
        <h2 className="text-xl">How do you feel today? 💭</h2>
        <Select onValueChange={(value) => setSelectedEmotion(value)}>
          {Object.keys(emotions).map((emotion) => (
            <SelectItem key={emotion} value={emotion}>{emotion}</SelectItem>
          ))}
        </Select>
        {selectedEmotion && <p className="mt-2 text-green-700">{emotions[selectedEmotion]}</p>}
      </div>

      <div className="my-6">
        <h2 className="text-xl">📚 Study Planner Generator</h2>
        <input
          type="number"
          className="border p-2 rounded"
          placeholder="Number of subjects"
          onChange={(e) => setStudySubjects([...Array(Number(e.target.value)).keys()])}
        />
        {studySubjects.map((_, index) => (
          <input key={index} className="border p-2 my-2 rounded" placeholder={`Subject ${index + 1}`} />
        ))}
        <Button className="mt-2">Generate Plan</Button>
      </div>

      <div className="my-6">
        <h2 className="text-xl">⏳ Study Timer</h2>
        <input
          type="number"
          className="border p-2 rounded"
          placeholder="Minutes"
          onChange={(e) => setTimer(Number(e.target.value))}
        />
        <Button className="mt-2">Start Timer</Button>
      </div>
    </div>
  );
};

export default MindEase;
