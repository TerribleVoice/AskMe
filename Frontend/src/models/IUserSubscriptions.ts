export interface IUserSubscriptions {
  id: string;
  authorId: string;
  price: number;
  name: string;
  description: string;
  isBought: boolean;
  isInherit: boolean;
  parentSubscriptionId?: string;
}
export type IUserCreateSubscription = Omit<
  IUserSubscriptions,
  "id" | "parentSubscriptionId" | "isBought" | "isInherit"
>;
export type IUserEditSubscription = IUserCreateSubscription;
