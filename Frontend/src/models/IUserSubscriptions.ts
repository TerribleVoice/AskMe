export interface IUserSubscriptions {
  id: string;
  authorId: string;
  price: number;
  name: string;
  description: string;
  parentSubscriptionId?: string;
}
export type IUserCreateSubscription = Omit<
  IUserSubscriptions,
  "id" | "authorId"
>;
