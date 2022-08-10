require 'rails_helper'

RSpec.describe Flavornote, type: :model do
  let(:user) { FactoryBot.create(:user) }
  let(:flavornote) { user.flavornotes.build(content: "チェリーのような甘酸っぱい風味") }

  it "有効であること" do
    expect(flavornote).to be_valid
  end

  it "user_idがない場合は無効であること" do
    flavornote.user_id = nil
    expect(flavornote).not_to be_valid
  end

  describe "content" do
    it "空なら無効であること" do
      flavornote.content = "   "
      expect(flavornote).not_to be_valid
    end

    it "141文字以上なら無効であること" do
      flavornote.content = "a" * 141
      expect(flavornote).not_to be_valid
    end
  end
end
