# Reward Hacking

Agent/Model learns an unintentional (undesirable) behaviour to achieve the high reward.&#x20;

This happens because:

* We thought that the given reward will induce some particular kind of behaviour that we want the agent to execute to complete the task.&#x20;
  * But the agents completes the task (achieves high reward) but by using the behaviour that's not be wanted because of a few reasons.
* Reward hacking can happen because Reward doesn't have 1-to-1 mapping withe policy. Multiple policies can achieve same reward.&#x20;
* It is related to problem of reward misspecification.&#x20;
* For example, give a bipedal agent, the reward is 1 for covering some distance forward which corresponds to task of moving forward, there's multiple policy possible
  * Walk
  * Crawl
  * Roll
  * But out of all these, for us, we maybe only intended for the agent to use walk policy and other's are undesirable.&#x20;
