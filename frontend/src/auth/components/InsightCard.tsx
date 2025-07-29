export const InsightCard = () => {
  return (
    <div className="bg-purple-50 rounded-2xl p-6 mb-6">
      <div className="flex items-start gap-4">
        <div className="w-10 h-10 bg-white/80 rounded-xl flex items-center justify-center flex-shrink-0">
          <i className="fas fa-lightbulb text-kinri-primary"></i>
        </div>
        <div className="flex-1">
          <h3 className="font-medium text-gray-800 mb-2">Recent Insight</h3>
          <p className="text-gray-700 font-light leading-relaxed">
            "You've shown remarkable progress in recognizing your emotional patterns.
            Your mindfulness practice is creating positive shifts in how you respond to
            stress."
          </p>
        </div>
      </div>
    </div>
  )
}
