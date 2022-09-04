require 'rails_helper'

RSpec.describe "Sessions", type: :system do
    before do
        driven_by(:rack_test)
    end

    describe '#new' do
        context '無効な値の場合' do
            it 'flashメッセエージが表示されること' do
                visit login_path

                fill_in 'メールアドレス', with: ''
                fill_in 'パスワード', with: ''
                click_button 'ログインする'

                expect(page).to have_selector 'div.alert.alert-danger'

                visit root_path
                expect(page).to_not have_selector 'div.alert.alert-danger'
            end
        end
    end
end