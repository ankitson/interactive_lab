class AddTimeToUsers < ActiveRecord::Migration
  def self.up
    add_column :users, :time, :string
  end

  def self.down
    remove_column :users, :time
  end
end
